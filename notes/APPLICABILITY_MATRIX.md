# Applicability Matrix

The framework applies to finite graphs directly and to geometric objects
only after a documented graph extraction. The extraction can discard
information, so a successful graph test is not automatically a theorem
about the source object.

| Object | Directly testable here? | Required representation | Main information lost |
| --- | --- | --- | --- |
| Finite simple graph | Yes | Adjacency sets | None |
| Planar map or knot projection graph | Yes, after extraction | Projection, Tait, Seifert, or region graph | Over/under data unless retained separately |
| Weighted graph | Partly | Thresholded or support graph | Weights unless analyzed separately |
| Directed graph | Partly | Underlying simple graph or directed extension | Direction in the simple projection |
| Multigraph | Partly | Simplified graph or explicit extension | Edge multiplicity in the simple projection |
| Partition/coarse-graining graph | Yes as a diagnostic | Cell adjacency or transition graph | Geometry inside each cell |
| Magnetic flux tubes or Maxwell field lines | Only indirectly | Sampled curves plus linking/adjacency graph | Field strength, helicity, embedding, and dynamics |
| Knot or link type | No, not by graph statistics alone | Graph diagnostic plus knot invariants | Ambient-isotopy information |
| Green's shift-graph step | Yes for finite instances | `G_(m,k)` | Nilsystem and recurrence analysis |

For the graphs already studied in the broader project, cycle profiles,
colorability, spectra, and partition sensitivity are reasonable
experiments. Closed formulas from the boundary-layer obstruction apply
only when the extracted graph is actually isomorphic to
`S(K_(q,2q^4))`.
