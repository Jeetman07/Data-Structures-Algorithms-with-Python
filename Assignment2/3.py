from __future__ import annotations
import ctypes

class ReservedMemory():
    def __init__(self, size: int) -> None:
        if not isinstance(size, int):
            raise(TypeError('Memory size must be a positive integer > 0!'))
        if not 1 <= size <= 65536:
            raise(ValueError('Reserved memory size must be between 1 and 65536 bytes!'))
        
        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self) -> int:
        return len(self._reserved_memory)

    def __repr__(self) -> str:
        l = len(self._reserved_memory)
        plural = 's' if l > 1 else ''
        str_repr = f"[{', '.join(str(ord(i)) for i in self._reserved_memory)}]"
        return f"ReservedMemory ({l} byte{plural}): {str_repr}"

    def copy(self, mem_source, count: int = None, source_index: int = 0, destination_index: int = 0) -> None:
        if not isinstance(mem_source, ReservedMemory):
            return TypeError('Source object must be a ReservedMemory object')

        if count is None:
            count = len(mem_source._reserved_memory) - source_index
        elif not isinstance(count, int) or count <= 0:
            return ValueError('Count must be a positive integer > 0')

        self._reserved_memory[destination_index:destination_index+count] = \
            mem_source._reserved_memory[source_index:source_index+count]

    def __getitem__(self, k: int) -> int:
        if not isinstance(k, int):
            raise TypeError('Index must be a positive integer >= 0')
        elif not 0 <= k < len(self._reserved_memory):
            raise IndexError('Index is out of bounds!')
        return ord(self._reserved_memory[k])

    def __setitem__(self, k: int, val: int) -> None:
        if not isinstance(k, int):
            raise TypeError('Index must be a positive integer >= 0')
        elif not (0 <= k < len(self._reserved_memory)):
            raise IndexError('Index is out of bounds!')
        self._reserved_memory[k] = val


class IntArray():
    def __init__(self, bytes_per_element: int = 2) -> None:
        self._resmem = None
        self._size = 0
        self._bytes_per_element = bytes_per_element
        self._shift_val = 2 ** ((self._bytes_per_element * 8) - 1)
        self._min_val = -self._shift_val
        self._max_val = self._shift_val - 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self) -> int:
        if self._iter_index < self._size:
            self._iter_index += 1
            return self[self._iter_index - 1]
        raise StopIteration

    def __repr__(self) -> str:
        if not self._resmem:
            return "Empty IntArray"
        l = self._size
        plural = 's' if l > 1 else ''
        str_repr = f"[{', '.join(str(v) for v in self)}]"
        return f"IntArray ({l} element{plural}): {str_repr}"

    def __setitem__(self, k: int, val: int) -> None:
        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError(f'Value must be an integer between {self._min_val} and {self._max_val}')

        val_to_store = val + self._shift_val
        for byte_index in range(self._bytes_per_element):
            self._resmem[k * self._bytes_per_element + byte_index] = \
                (val_to_store >> (8 * byte_index)) & 255

    def __getitem__(self, k: int) -> int:
        stored_val = 0
        for byte_index in range(self._bytes_per_element):
            stored_val |= self._resmem[k * self._bytes_per_element + byte_index] << (8 * byte_index)
        return stored_val - self._shift_val

    def append(self, val: int) -> None:
        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError(f'Value must be an integer between {self._min_val} and {self._max_val}')

        self._size += 1
        new_resmem = ReservedMemory(self._size * self._bytes_per_element)

        if self._resmem:
            new_resmem.copy(self._resmem)

        self._resmem = new_resmem
        self[self._size - 1] = val

    def pop(self) -> int:
        if self._size == 0:
            return None

        val = self[self._size - 1]
        self._size -= 1

        if self._size > 0:
            new_resmem = ReservedMemory(self._size * self._bytes_per_element)
            new_resmem.copy(self._resmem, count=self._size * self._bytes_per_element)
        else:
            new_resmem = None

        self._resmem = new_resmem
        return val

    def search(self, value):
        """
        Search method for the array

        Parameters:
        - 'value': value to search

        Returns:
          First index position where the value is found or -1 if not found
        """
        for i in range(self._size):
            if self[i] == value:
                return i
        return -1
