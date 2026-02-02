def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    pairs = []

    for num in numbers:
        if num % 2 == 0:  # even
            odd = odd_queue.dequeue()
            if odd is not None:
                pairs.append((num, odd))
            else:
                even_queue.enqueue(num)
        else:  # odd
            even = even_queue.dequeue()
            if even is not None:
                pairs.append((even, num))
            else:
                odd_queue.enqueue(num)

    return pairs
