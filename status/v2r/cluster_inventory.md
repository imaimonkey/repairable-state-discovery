# V2R cluster inventory

2026-09-25T22:18:51.030166+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318695600128 available bytes; 82.22% used; 112476303 free inodes.

server1 `/home`: 318695600128 available bytes; 82.22% used; 112476303 free inodes.

server1 `/tmp`: 318695600128 available bytes; 82.22% used; 112476303 free inodes.

server1 `/var/tmp`: 318695600128 available bytes; 82.22% used; 112476303 free inodes.

server1 `/mnt/raid5`: 360269271040 available bytes; 98.35% used; 337539003 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22947762176 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22947762176 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22947762176 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22947762176 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 299302965248 available bytes; 97.93% used; 445053273 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 84359671808 available bytes; 95.29% used; 114152636 free inodes.

server3 `/home`: 84359671808 available bytes; 95.29% used; 114152636 free inodes.

server3 `/data`: 124826066944 available bytes; 98.27% used; 225806154 free inodes.

server3 `/tmp`: 84359671808 available bytes; 95.29% used; 114152636 free inodes.

server3 `/var/tmp`: 84359671808 available bytes; 95.29% used; 114152636 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105311981568 available bytes; 94.12% used; 114347142 free inodes.

server4 `/home`: 105311981568 available bytes; 94.12% used; 114347142 free inodes.

server4 `/data`: 205913231360 available bytes; 97.15% used; 224917901 free inodes.

server4 `/tmp`: 105311981568 available bytes; 94.12% used; 114347142 free inodes.

server4 `/var/tmp`: 105311981568 available bytes; 94.12% used; 114347142 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
