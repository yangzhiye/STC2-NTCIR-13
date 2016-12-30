# -*- coding: utf-8 -*-
import thulac

thu1 = thulac.thulac("-seg_only")

print " ".join(thu1.cut("我爱北京天安门,杨志烨无敌!?"))

print len("他")