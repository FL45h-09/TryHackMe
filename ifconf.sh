#!/bin/bash

ip -4 addr show tun0 | grep -oP "(?<=inet ).*(?=/)"

