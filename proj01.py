"""
Project 1 - Doubly Linked Lists
CSE 331 SS25
"""

from __future__ import annotations
from typing import List, TypeVar, Tuple, Optional

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")

# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    DO NOT MODIFY
    """
    __slots__ = ["value", "next", "prev"]

    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        DO NOT MODIFY
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        DO NOT MODIFY
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Return boolean indicating whether DLL is empty.

        :return: True if DLL is empty, else False.
        """
        return self.size == 0

    def push(self, val: T, back: bool = True) -> None:
        """
        Create Node containing `val` and add to back (or front) of DLL. Increment size by one.

        :param val: value to be added to the DLL.
        :param back: if True, add Node containing value to back (tail-end) of DLL;
            if False, add to front (head-end).
        :return: None.
        """
        newnode = Node(val)
        if self.size == 0:
            self.tail = newnode
            self.head = newnode
            self.head.prev = None
            self.tail.next = None

        elif back is True:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
            self.tail.next = None

        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
            self.head.prev = None

        self.size += 1

    def pop(self, back: bool = True) -> None:
        """
        Remove Node from back (or front) of DLL. Decrement size by 1. If DLL is empty, do nothing.

        :param back: if True, remove Node from (tail-end) of DLL;
            if False, remove from front (head-end).
        :return: None.
        """
        if self.size == 0:
            pass

        elif self.head == self.tail:
            self.head = self.tail = None
            self.size -= 1

        elif back is True:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1

        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

    def list_to_dll(self, source: List[T]) -> None:
        """
        Construct DLL from a standard Python list.

        :param source: standard Python list from which to construct DLL.
        :return: None.
        """
        self.head = self.tail = None
        self.size = 0
        for item in source:
            new_node = Node(item)
            self.push(item)

    def dll_to_list(self) -> List[T]:
        """
        Construct standard Python list from DLL.

        :return: standard Python list containing values stored in DLL.
        """
        temp = self.head
        newlst = []
        while temp is not None:
            newlst.append(temp.value)
            temp = temp.next
        return newlst

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Construct list of Nodes with value val in the DLL and return the associated Node list

        :param val: The value to be found
        :param find_first: If True, only return the first occurrence of val. If False, return all
        occurrences of val
        :return: A list of all the Nodes with value val.
        """
        temp = self.head
        newlst = []
        while temp is not None:
            if temp.value == val:
                newlst.append(temp)
                if find_first is True:
                    return newlst
            temp = temp.next
        return newlst

    def find(self, val: T) -> Node:
        """
        Find first instance of `val` in the DLL and return associated Node object..

        :param val: value to be found in DLL.
        :return: first Node object in DLL containing `val`.
            If `val` does not exist in DLL, return an empty list.
        """
        newlst = self._find_nodes(val)
        if len(newlst) == 0:
            return None
        else:
            return newlst[0]


    def find_all(self, val: T) -> List[Node]:
        """
        Find all instances of `val` in DLL and return Node objects in standard Python list.

        :param val: value to be searched for in DLL.
        :return: Python list of all Node objects in DLL containing `val`.
            If `val` does not exist in DLL, return None.
        """
        nodelst = self._find_nodes(val)
        if len(nodelst) == 0:
            return []
        return nodelst

    def remove_node(self, to_remove: Node) -> None:
        """
        Given a node in the linked list, remove it.

        :param to_remove: node to be removed from the list
        :return: None
        """
        if to_remove == self.head and to_remove == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1

        elif to_remove == self.head:
            self.head = to_remove.next
            if self.head:
                self.head.prev = None
            to_remove.next = None
            self.size -= 1

        elif to_remove == self.tail:
            self.tail = to_remove.prev
            self.tail.next = None
            self.size -= 1

        elif self.size == 1:
            self.head = self.tail = None
            self.size -= 1

        else:
            before = to_remove.prev
            after = to_remove.next
            to_remove.prev = None
            to_remove.next = None
            if before is not None:
                before.next = after
            if after is not None:
                after.prev = before
            to_remove.prev = None
            to_remove.next = None
            self.size -= 1

    def remove(self, val: T) -> bool:
        """
        Delete first instance of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: True if Node containing `val` was deleted from DLL; else, False.
        """
        if self.find(val):
            holder = self.head
            while holder is not None:
                if holder.value == val:
                    self.remove_node(holder)
                    return True
                holder = holder.next

        else:
            return False

    def remove_all(self, val: T) -> int:
        """
        Delete all instances of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: integer indicating the number of Nodes containing `val` deleted from DLL;
                 if no Node containing `val` exists in DLL, return 0.
        """
        nums_removed = 0
        holder = self.head
        while holder is not None:
            if holder.value == val:
                otherhold = holder
                holder = holder.next
                self.remove_node(otherhold)
                nums_removed += 1
            else:
                holder = holder.next
        return nums_removed

    def reverse(self) -> None:
        """
        Reverse DLL in-place by modifying all `next` and `prev` references of Nodes in the
        DLL and resetting the `head` and `tail` references.

        :return: None.
        """
        if self.head is None:
            return None

        holder = self.head
        while holder is not None:
            temp = holder.next
            holder.next = holder.prev
            holder.prev = temp
            holder = holder.prev  # going foward in the list

        temp = self.head
        self.head = self.tail
        self.tail = temp


class Spotify_Music_Player:
    def __init__(self, paid: bool=False) -> None:
        """
        Initializes the Spotify_Music_Player class

        :param paid: Account type for Spotify
        :return: None
        """
        self.songlist = DLL()
        self.playing: Optional[Node] = None
        self.paid = paid

    def play_favorite_next(self, favorite_song, forward=True) -> None:
        """
        Changes the song order so that the favorite sone is played after the current one

        :param favorite_song: Song to be played next
        :param forward: This tells you where to remove the favorite song node from, in order to move it after the currently playing song, if already in the song list. If True, remove latest node in the tree that contains the favorite song. If False, remove the first occurence of favorite song and move it to be after the playing node.
        :return: None
        """
        if self.playing is None:
            self.songlist.push(favorite_song)
            self.playing = self.songlist.tail
            return

        all_favorite = self.songlist.find_all(favorite_song)
        if all_favorite:
            if forward:
                node_to_remove = all_favorite[-1]
            else:
                node_to_remove = all_favorite[0]
            self.songlist.remove(node_to_remove)
        else:
            node_to_remove = Node(favorite_song)
            self.songlist.size += 1

        if node_to_remove in all_favorite:
            self.songlist.remove_node(node_to_remove)

        currnext = self.playing.next

        self.playing.next = node_to_remove
        node_to_remove.prev = self.playing

        node_to_remove.next = currnext
        if currnext:
            currnext.prev = node_to_remove
        else:
            self.songlist.tail = node_to_remove

    def add_ads(self, advertisement: str, favorite: str) ->None:
        """
        Inserts ads for non-premium Spotify accounts

        :param advertisement: Value of ad to be inserted.
        :param favorite: User's favorite song so ad can be inserted after it.
        """
        if self.paid is True:
            return

        newnode = self.songlist.head

        while newnode is not None:
            if newnode.value == favorite:
                try:
                    if newnode.prev.value == favorite:
                        break
                except AttributeError:
                    pass
                if newnode.prev is None or newnode.prev.value != advertisement:
                    ad = Node(advertisement)
                    ad.next = newnode
                    ad.prev = newnode.prev
                    if newnode.prev:
                        newnode.prev.next = ad
                    else:
                        self.songlist.head = ad
                    newnode.prev = ad
                    self.songlist.size += 1

            newnode = newnode.next
