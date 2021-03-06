import chainer


class MidLevelNetwork(chainer.Chain):
    def __init__(self):
        super(MidLevelNetwork, self).__init__(
            conv1_1=chainer.links.Convolution2D(
                in_channels=None,
                out_channels=512,
                ksize=3,
                stride=1,
                pad=1),
            bn1_1=chainer.links.BatchNormalization(512),
            conv1_2=chainer.links.Convolution2D(
                in_channels=None,
                out_channels=256,
                ksize=3,
                stride=1,
                pad=1),
            bn1_2=chainer.links.BatchNormalization(256),
        )

    def __call__(self, x, test=False):
        # type: (any, bool) -> any
        h = x
        h = chainer.functions.relu(self.bn1_1(self.conv1_1(h)))
        h = chainer.functions.relu(self.bn1_2(self.conv1_2(h)))
        return h
