@testset "{{ name.title() }} Tests" begin

  @test {{ name.title() }}(42, 0).bar == 42

end
