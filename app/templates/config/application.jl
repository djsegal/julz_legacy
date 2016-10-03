__precompile__()

module Application
  include("include_all.jl")
  include("export_all.jl")

  include_all("app")
  @export_all

  function main()
    println("done.")
  end
end
