# V2R cluster inventory

2026-09-27T07:29:31.004476+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314478714880 available bytes; 82.46% used; 112440787 free inodes.

server1 `/home`: 314478714880 available bytes; 82.46% used; 112440787 free inodes.

server1 `/tmp`: 314478714880 available bytes; 82.46% used; 112440787 free inodes.

server1 `/var/tmp`: 314478714880 available bytes; 82.46% used; 112440787 free inodes.

server1 `/mnt/raid5`: 634660950016 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['0', '1'] | [] | reference_compatible=False |

server2 `/`: 17615060992 available bytes; 99.02% used; 110365012 free inodes.

server2 `/home`: 17615060992 available bytes; 99.02% used; 110365012 free inodes.

server2 `/tmp`: 17615060992 available bytes; 99.02% used; 110365012 free inodes.

server2 `/var/tmp`: 17615060992 available bytes; 99.02% used; 110365012 free inodes.

server2 `/mnt/raid5`: 571408683008 available bytes; 96.05% used; 444874246 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 78572978176 available bytes; 95.62% used; 114062879 free inodes.

server3 `/home`: 78572978176 available bytes; 95.62% used; 114062879 free inodes.

server3 `/data`: 1333035175936 available bytes; 81.58% used; 225764087 free inodes.

server3 `/tmp`: 78572978176 available bytes; 95.62% used; 114062879 free inodes.

server3 `/var/tmp`: 78572978176 available bytes; 95.62% used; 114062879 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111070531584 available bytes; 93.80% used; 114372889 free inodes.

server4 `/home`: 111070531584 available bytes; 93.80% used; 114372889 free inodes.

server4 `/data`: 374343090176 available bytes; 94.83% used; 224771052 free inodes.

server4 `/tmp`: 111070531584 available bytes; 93.80% used; 114372889 free inodes.

server4 `/var/tmp`: 111070531584 available bytes; 93.80% used; 114372889 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
