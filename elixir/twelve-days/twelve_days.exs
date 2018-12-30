defmodule TwelveDays do

  @number %{
    1 => "first",
    2 => "second",
    3 => "third",
    4 => "fourth",
    5 => "fifth",
    6 => "sixth",
    7 => "seventh",
    8 => "eighth",
    9 => "ninth",
    10 => "tenth",
    11 => "eleventh",
    12 => "twelfth",
  }

  @verse %{
    1 => "a Partridge in a Pear Tree.",
    2 => "two Turtle Doves, ",
    3 => "three French Hens, ",
    4 => "four Calling Birds, ",
    5 => "five Gold Rings, ",
    6 => "six Geese-a-Laying, ",
    7 => "seven Swans-a-Swimming, ",
    8 => "eight Maids-a-Milking, ",
    9 => "nine Ladies Dancing, ",
    10 => "ten Lords-a-Leaping, ",
    11 => "eleven Pipers Piping, ",
    12 => "twelve Drummers Drumming, ",
  }

  @doc """
  Given a `number`, return the song's verse for that specific day, including
  all gifts for previous days in the same line.
  """
  @spec verse(number :: Integer.t) :: String.t
  def verse(number) do

    case number do
      1 ->
        Map.put(@verse, number, "a Partridge in a Pear Tree.")
      _ ->
        Map.put(@verse, number, "and a Partridge in a Pear Tree.")
    end

    "On the #{Map.get(@number, number)} day of Christmas my true love gave to me: #{Enum.join(Enum.map(number..1, &Map.get(@verse, &1)))}"
  end

  @doc """
  Given a `starting_verse` and an `ending_verse`, return the verses for each
  included day, one per line.
  """
  @spec verses(starting_verse :: Integer.t, ending_verse :: Integer.t) :: String.t
  def verses(starting_verse, ending_verse) do
    Enum.join(Enum.map(starting_verse..ending_verse, &verse(&1)), "\n")
  end

  @doc """
  Sing all 12 verses, in order, one verse per line.
  """
  @spec sing() :: String.t
  def sing do
    verses(1, 12)
  end
end
