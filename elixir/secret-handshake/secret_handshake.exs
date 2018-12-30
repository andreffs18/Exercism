defmodule SecretHandshake do
  @doc """
  Determine the actions of a secret handshake based on the binary
  representation of the given `code`.

  If the following bits are set, include the corresponding action in your list
  of commands, in order from lowest to highest.

  1 = wink
  10 = double blink
  100 = close your eyes
  1000 = jump

  10000 = Reverse the order of the operations in the secret handshake
  """

  use Bitwise, only_operators: true

  @handshakes %{
    1 => "wink",
    2 => "double blink",
    4 => "close your eyes",
    8 => "jump"
  }

  @spec commands(code :: Integer.t) :: list(String.t)
  def commands(code) do
    @handshakes
    |> Enum.filter(fn {bitcode, _} -> (code &&& bitcode) != 0 end)
    |> Enum.map(&Tuple.to_list/1)
    |> Enum.map(&List.last/1)
    |> reverse(code)
  end

  @spec reverse(handshakes :: list(String.t), code :: Integer.t) :: list(String.t)
  defp reverse([], _) do [] end
  defp reverse(handshakes, code) when (code &&& 16) == 0 do handshakes end
  defp reverse(handshakes, code) when (code &&& 16) != 0 do Enum.reverse(handshakes) end

end