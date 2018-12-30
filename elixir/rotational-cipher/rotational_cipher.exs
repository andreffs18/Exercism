defmodule RotationalCipher do
  @doc """
  Given a plaintext and amount to shift by, return a rotated string.

  Example:
  iex> RotationalCipher.rotate("Attack at dawn", 13)
  "Nggnpx ng qnja"
  """
  @spec rotate(text :: String.t, shift :: Integer.t) :: String.t
  def rotate(text, shift) do
    text
    |> String.to_charlist
    |> Enum.map(&add_shift(&1, shift))
    |> List.to_string
  end

  @spec add_shift(char :: Char.t, shift :: Integer.t) :: Char.t
  defp add_shift(char, shift) when char in ?a..?z do
    rem((char - ?a) + shift, 26) + ?a
  end
  defp add_shift(char, shift) when char in ?A..?Z do
    rem((char - ?A) + shift, 26) + ?A
  end
  defp add_shift(char, _), do: char
end
