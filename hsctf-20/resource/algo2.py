#!/usr/bin/env python3
# -*- coding: utf-8 -*-


area = 70368744177664

total_area = 0

for i in range(1,26):
    total_area += (area/i)*i

print("flag{%d}"%total_area)

print("flag{%d}"%(70368744177664*25))