import os
import sys
import cv2
import random
from typing import Any
from typing import List
from typing import Tuple
from typing import Optional
from typing import Iterator
from dataclasses import dataclass


@dataclass
class Base:
    images: List[str]
    labels: List[str]
    classes: List[str]
    
    def __len__(self) -> int:
        """ Returns the number of images in the dataset. """
        return len(self.images)

    def __getitem__(self, index) -> Base:
        """
        Retrieves an item or a list of items from the dataset based on the given index or indices.

        This method supports accessing dataset elements via integer indices or slices. When given an integer,
        it converts the integer to a list containing that index to maintain consistency in the returned object's structure.
        It then constructs and returns an instance of the `Base` class populated with the corresponding image data,
        labels, and classes for the specified index or indices.

        Parameters:
            index (int | slice): The index of the item to retrieve from the dataset. Can be an integer for a single item
            or a slice object for retrieving multiple items.

        Returns:
            Base: An instance of the `Base` class containing the requested image(s), label(s), and class(es). The `Base`
            class is expected to be a structure that can hold and organize these types of data.

        Raises:
            IndexError: If the provided index is out of the bounds of the dataset.

        Example:
            >>> dataset = DatasetClass(...)
            >>> item = dataset[0]  # Retrieve the first item
            >>> batch = dataset[0:5]  # Retrieve the first five items as a batch
        """

        if isinstance(index, int):
            index = [index]
        return Base(
            image=(np.array(self.images)[index]).tolist(),
            labels=(np.array(self.labels)[index]).tolist(),
            classes=(np.array(self.classes)[index]).tolist(),
        )

    def __iter__(
        self
    ) -> Iterator[
        Tuple[
            List[str],
            List[str],
            List[str],
        ]
    ]:
        """
        Provides an iterator over the object's data, yielding tuples of images, labels, and classes.

        This method allows the object to be iterated over in a for-loop or other iterator contexts, 
        returning a tuple for each iteration. Each tuple consists of lists of image data, associated labels, 
        and class identifiers, respectively. This facilitates easy access to the object's collection of images, 
        their labels, and classes in a structured format.

        Yields:
            Iterator[Tuple[List[str], List[str], List[str]]]: An iterator that yields a tuple containing 
            three lists for each iteration. The first list contains image data, the second list contains labels 
            corresponding to each image, and the third list contains class identifiers for each image.

        Example:
            >>> dataset = YourDatasetClass(...)  # Assuming this is part of a dataset class
            >>> for image_data, labels, classes in dataset:
            >>>     process(image_data, labels, classes)
            # This loop will go through all items in the dataset, allowing you to process each set of image data, labels, and classes.
        """
        for i in range(len(self.images)):
            yield (
                self.image[i],
                self.labels[i],
                self.classes[i],
            )

    def train_val_split(
        self, split_ratio:int=.8,
        random_state:Optional[int]=None,
        shuffle:Optional[bool]=True,
    ):
        """
        Splits the dataset into training and validation (test) sets based on the given split ratio.

        This method partitions the dataset into two subsets: one for training and one for validation/testing. 
        It optionally shuffles the dataset before splitting if specified. The shuffling process can be made 
        deterministic by setting a random state.

        Parameters:
            split_ratio (float, optional): The proportion of the dataset to include in the train split. 
                Defaults to 0.8, meaning 80% of the data is used for training and the rest for validation/testing.
            random_state (Optional[int], optional): A seed for the random number generator to ensure reproducible 
                shuffling. If None, the random number generator is the RandomState instance used by `np.random`. 
                Defaults to None.
            shuffle (bool, optional): Whether or not to shuffle the data before splitting. Defaults to True.

        Returns:
            tuple: Two subsets of the dataset, the first being the training set and the second the validation (test) set.

        Example:
            >>> dataset = DatasetClass(...)
            >>> train_ds, test_ds = dataset.train_val_split(split_ratio=0.75, random_state=42)
        """
        indexes = np.arange(0, len(self.images),  1)
        if not random_state is None:
            random.seed(random_state)
        
        if shuffle:
            random.shuffle(indexes)

        split_index = int(len(self.images) * split_ratio)
        train_split, test_split = indexes[:split_index], indexes[split_index:]

        train_ds = Base[train_split]
        test_ds = Base[test_split]

        return train_ds, test_ds



    