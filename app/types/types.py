dsp_types = """


type Acceleration {
  id: ID!
  x: Float
  y: Float
  z: Float
}

input AccelerationAsInput {
  id: ID!
  x: Float
  y: Float
  z: Float
}



enum AggregateOp {
  MIN
  MAX
  SUM
  COUNT
}

scalar Date

scalar DateTime

type FFTInput {
  id: ID!
  values: [Float]!
}

input FFTInputAsInput {
  id: ID!
  values: [Float!]!
}

type FFTMagnitude {
  id: ID!
  value: Float!
}

input FFTMagnitudeAsInput {
  id: ID!
  value: Float!
}

type FFTMagnitudeOutput {
  id: ID!
  value: Float!
}

type Filter {
  id: ID!
  filterOrder: Int!
  filterFrequencies: FilterFrequencies!
  function: FilterFunction!
}

input FilterAsInput {
  id: ID!
  filterOrder: Int!
  filterFrequencies: FilterFrequenciesAsInput!
  function: FilterFunctionAsInput!
}

type FilteredResult {
  id: ID!
  values: [Float!]!
}

type FilterFrequencies {
  id: ID!
  lowCutOff: Frequency!
  highCutOff: Frequency!
  samplingFrequency: Frequency!
}

input FilterFrequenciesAsInput {
  id: ID!
  lowCutOff: FrequencyAsInput!
  highCutOff: FrequencyAsInput!
  samplingFrequency: FrequencyAsInput!
}

type FilterFunction {
  id: ID!
}

input FilterFunctionAsInput {
  id: ID!
}

type Frequency {
  id: ID!
  value: Float!
  unit: String!
}

input FrequencyAsInput {
  id: ID!
  value: Float!
  unit: String!
}

type IIRFilterPolynomials {
  id: ID!
  numerator: [Float!]!
  denominator: [Float!]!
}

input IIRFilterPolynomialsAsInput {
  id: ID!
  numerator: [Float!]!
  denominator: [Float!]!
}

type Impact {
  id: ID!
  positive: Boolean!
}

type Info {
  id: ID!
  name: String!
  description: String
}


type Intensity {
  id: ID!
  value: Float!
}

input IntensityAsInput {
  id: ID!
  value: Float!
}

scalar JSON

type Query {

  computeResultant(accelerations: [AccelerationAsInput!]!): [Resultant!]!
  computeIntensity(fftMagnitudes: [FFTMagnitudeAsInput], filter: FilterAsInput, fftpoints: Int!): Intensity
  makeButterworthFilter(filter: FilterAsInput): IIRFilterPolynomials
  lfilter1D(iirFilterPolynomials: IIRFilterPolynomialsAsInput, dataToFilter: [Float]): FilteredResult
  computeImpact(intensity: IntensityAsInput!): Impact!
  compute1DDFT(input: [FFTInputAsInput!]!, points: Int!): [FFTMagnitudeOutput!]!
  createData: Boolean
  projectData: [Acceleration]
  CKGErrors: [String]
}

type Resultant {
  id: ID!
  value: Float
}

input ResultantAsInput {
  id: ID!
  value: Float
}

scalar Time



"""