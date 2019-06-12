import pytest
import final


def test_is_palindrome():
    assert final.is_palindrome(123454321)


def test_happy_ending():
    assert final.happy_ending() == 2


def test_final_ending():
    assert final.final_ending() == 2


def test_dice_roll():
    roll = final.dice_roll(10)
    assert roll > 0 and roll < 11


def test_player_init():
    test_player = final.player(10, 5, "name")
    assert test_player.max_health == 10


def character_innit():
    test_character = final.characters(5, 10, "name")
    assert test_character.health == 5
    assert test_character.damage == 10
    assert test_character.name == "name"

