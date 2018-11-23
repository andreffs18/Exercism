defmodule Words do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t) :: Map.t
  def count(sentence) when is_binary(sentence) do
    words = Regex.replace(~r/[$^=:&!?@_,;%]/, sentence, " ")
    |> String.downcase()
    |> String.split()

    Enum.reduce(words, %{}, fn word, counter ->
      Map.put(counter, word, Enum.count(words, &(&1 == word))) end)
  end
end
