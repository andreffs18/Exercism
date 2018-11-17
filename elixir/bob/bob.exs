defmodule Bob do

  def hey(input) do
    cond do
      silence?(input) ->
        "Fine. Be that way!"
      yell?(input) and question?(input) ->
        "Calm down, I know what I'm doing!"
      question?(input) ->
        "Sure."
      yell?(input) ->
        "Whoa, chill out!"
      true ->
        "Whatever."
    end
  end

  defp yell?(input) do String.upcase(input) == input and String.match?(input, ~r/\p{L}+/) end
  defp silence?(input) do String.trim(input) == "" end
  defp question?(input) do String.ends_with?(input, "?") end
end
