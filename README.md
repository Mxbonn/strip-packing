# About Strip-Packing
This repository contains implementations for the strip packing problem.

The strip packing problem optimizes the placing of rectangles in a strip of fixed width and variable length, such that the overall length of the strip is minimised.

Currently the 'Priority Heuristic' algorithm is implemented for the variant in which rotations are allowed and cuts have to follow the guillotine constraint.
This is implemented in the `phspprg` method.
More information about parameters and return values can be found in the docstrings in the source.

**note:** This algorithm is heuristic which means that the outcome is possibly not the most optimal.

This algorithms is based on the following paper: **A priority heuristic for the guillotine rectangular packing problem**
```
@article{zhang2016priority,
  title={A priority heuristic for the guillotine rectangular packing problem},
  author={Zhang, Defu and Shi, Leyuan and Leung, Stephen CH and Wu, Tao},
  journal={Information Processing Letters},
  volume={116},
  number={1},
  pages={15--21},
  year={2016},
  publisher={Elsevier}
}
```

The results can be visualized with the `visualize` method, **matplotlib** needs to be installed for this.


## Example
`example.py` demonstrates an example, including visualization:
```python
    boxes = [
        [5, 3], [5, 3], [2, 4], [30, 8], [10, 20],
        [20, 10], [5, 5], [5, 5], [10, 10], [10, 5],
        [6, 4], [1, 10], [8, 4], [6, 6], [20, 14]
    ]
    width = 10
    height, rectangles = phspprg(width, boxes)
    visualize(width, height, rectangles)
    print("The height is: {}".format(height))

```

The output of the visualization is:

![Output of example](http://i.imgur.com/DhM96UK.png)

## Efficiency
It is important to realize that the algorithm is an heuristic and will not always find the optimal result.

The authors of the algorithm sort the rectangles internally by width, this is the most optimal for a lot of cases but not always.
Sometimes it can be much better to sort by height. This can be changed by setting the parameter `sorting='height'`.
The next outputs are an example how sorting can influence the result:

width
<img src="http://imgur.com/Fz73Kso.png" height="600" alt="Example when sorting by width">
vs height
<img src="http://imgur.com/WAjuk5D.png" height="600" alt="Example when sorting by height">

And it can also happen that none of the two sorting options result in THE optimal solution.

**Know the difference between heuristic and optimal when using this algorithm.**
