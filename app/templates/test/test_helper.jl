__precompile__()

module TestHelper
  include("../config/application.jl")

  using Reexport
  @reexport using .Application
  @reexport using Base.Test
  @export_all_except ["Application"]

  function main()
    @testset "All Tests" begin
      include_all("test", ".", true)
    end
  end
end
