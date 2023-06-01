import os, sys
import random, string, math
import socket, select, selectors, pickle
import json, csv
from colorama import Fore as f
from colorama import Back as b
import datetime
import asyncio, time, timeit
import uuid, hashlib, base64
from copy import deepcopy
import typing, types
import threading as thr
import _thread as thread
import msvcrt
import subprocess, shutil
import struct, re
import warnings
import zipapp, zipfile, gzip
import multiprocessing as mp
import urllib as ul
import urllib.request as ulr
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lockable")

GameHasEnded = False
running = True
GameWillEnd = False

# START OF The Lockable Requirements
LockableX = 800
LockableY = 800
LockableSize = 32
Lockable = pygame.Rect(random.randint(100, 700), random.randint(100, 700), LockableSize, LockableSize)
LockableColour = (0, 255, 0)
# END

lockables = 0
max_lockables = 20

text = ""
text_font = pygame.font.Font(None, 32)
text_box = pygame.Rect(250, 50, 100, 100)

Clock = pygame.time.Clock()

while running:
    Clock.tick(32)
    if not GameWillEnd:
        text = "Lockables Count: ({0}/{1})".format(lockables, max_lockables)
    if GameWillEnd:
        text = "Congratulations! you won"
        GameHasEnded = True
    pygame.draw.rect(screen, (0, 0, 0), text_box)
    rendered_text = text_font.render(text, False, (0, 0, 255))
    screen.blit(rendered_text, (text_box.x+5, text_box.y+5))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not GameWillEnd:
            PlayerMouse = pygame.mouse.get_pos()
            if PlayerMouse[0] <= Lockable.x + 32 or PlayerMouse[0] >= Lockable.x or PlayerMouse[1] <= Lockable.y + 32 or PlayerMouse[1] >= Lockable.y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, (255, 0, 0), Lockable)
                    lockables += 1
                    Lockable.update(random.randint(100, 700), random.randint(100, 700), LockableSize, LockableSize)

            if lockables > max_lockables:
                GameWillEnd = True

        pygame.draw.rect(screen, LockableColour, Lockable)

    pygame.display.update()
    screen.fill((0, 0, 0))

    if GameHasEnded:
        time.sleep(5)
        running = False

pygame.quit()
sys.exit(101)
