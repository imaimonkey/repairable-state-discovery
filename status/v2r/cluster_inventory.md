# V2R cluster inventory

2026-09-26T05:33:30.292467+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318791868416 available bytes; 82.22% used; 112476275 free inodes.

server1 `/home`: 318791868416 available bytes; 82.22% used; 112476275 free inodes.

server1 `/tmp`: 318791868416 available bytes; 82.22% used; 112476275 free inodes.

server1 `/var/tmp`: 318791868416 available bytes; 82.22% used; 112476275 free inodes.

server1 `/mnt/raid5`: 258978811904 available bytes; 98.81% used; 337541374 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22929960960 available bytes; 98.72% used; 110406217 free inodes.

server2 `/home`: 22929960960 available bytes; 98.72% used; 110406217 free inodes.

server2 `/tmp`: 22929960960 available bytes; 98.72% used; 110406217 free inodes.

server2 `/var/tmp`: 22929960960 available bytes; 98.72% used; 110406217 free inodes.

server2 `/mnt/raid5`: 276481581056 available bytes; 98.09% used; 445048805 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83076190208 available bytes; 95.36% used; 114125459 free inodes.

server3 `/home`: 83076190208 available bytes; 95.36% used; 114125459 free inodes.

server3 `/data`: 124341350400 available bytes; 98.28% used; 225824218 free inodes.

server3 `/tmp`: 83076190208 available bytes; 95.36% used; 114125459 free inodes.

server3 `/var/tmp`: 83076190208 available bytes; 95.36% used; 114125459 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094829568 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094829568 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 107012546560 available bytes; 98.52% used; 224929221 free inodes.

server4 `/tmp`: 106094829568 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094829568 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
