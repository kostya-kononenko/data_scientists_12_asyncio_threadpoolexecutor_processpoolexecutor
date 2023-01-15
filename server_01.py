import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 4000))
sock.listen()
print("Сервер працює.....")

while True:
    conn, add = sock.accept()
    print("Приєднався:", add)
    numbers = conn.recv(1024)
    numbers_decode = numbers.decode("UTF-8")
    numbers = numbers_decode.split()
    numbers = [int(i) for i in numbers]
    print('Перше отримане число:', numbers[0],
          'Друге отримане число:', numbers[1])

    async def multiplication_of_numbers():
        await asyncio.sleep(1)
        return numbers[0] * numbers[1]

    async def sum_of_numbers():
        await asyncio.sleep(1)
        return numbers[0] + numbers[1]

    async def number_difference():
        await asyncio.sleep(1)
        return numbers[0] - numbers[1]

    new_loop = asyncio.get_event_loop()

    tasks_all = [new_loop.create_task(multiplication_of_numbers()),
                 new_loop.create_task(sum_of_numbers()),
                 new_loop.create_task(number_difference())
                 ]
    tasks_wait = asyncio.wait(tasks_all)
    new_loop.run_until_complete(tasks_wait)

    message_for_client = ["Результат множення: " + str(tasks_all[0].result()),
                          "Результат складання: " + str(tasks_all[1].result()),
                          "Результат віднімання: " + str(tasks_all[2].result())
                          ]
    message_for_client = "\n".join(message_for_client)

    conn.send(bytes(message_for_client, encoding="UTF-8"))
    conn.close()
