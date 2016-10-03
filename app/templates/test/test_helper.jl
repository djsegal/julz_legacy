__precompile__()

module TestHelper
  include("../config/application.jl")
  using .Application
  using Base.Test

  function main()
    @testset "All Tests" begin
      include_all("test", ".", true)
    end
  end
end
