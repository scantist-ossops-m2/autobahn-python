# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers

class Challenge(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsChallenge(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Challenge()
        x.Init(buf, n + offset)
        return x

    # Challenge
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Challenge
    def Method(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Challenge
    def Extra(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Map import Map
            obj = Map()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def ChallengeStart(builder): builder.StartObject(2)
def ChallengeAddMethod(builder, method): builder.PrependUint8Slot(0, method, 0)
def ChallengeAddExtra(builder, extra): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(extra), 0)
def ChallengeEnd(builder): return builder.EndObject()