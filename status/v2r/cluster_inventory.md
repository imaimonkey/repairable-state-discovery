# V2R cluster inventory

2026-09-23T17:02:55.983905+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41391919104 available bytes; 97.69% used; 110435441 free inodes.

server2 `/home`: 41391919104 available bytes; 97.69% used; 110435441 free inodes.

server2 `/tmp`: 41391919104 available bytes; 97.69% used; 110435441 free inodes.

server2 `/var/tmp`: 41391919104 available bytes; 97.69% used; 110435441 free inodes.

server2 `/mnt/raid5`: 547622014976 available bytes; 96.22% used; 445216944 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294715981824 available bytes; 83.55% used; 114286183 free inodes.

server3 `/home`: 294715981824 available bytes; 83.55% used; 114286183 free inodes.

server3 `/data`: 53151338496 available bytes; 99.27% used; 225852939 free inodes.

server3 `/tmp`: 294715981824 available bytes; 83.55% used; 114286183 free inodes.

server3 `/var/tmp`: 294715981824 available bytes; 83.55% used; 114286183 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111489609728 available bytes; 93.78% used; 114375793 free inodes.

server4 `/home`: 111489609728 available bytes; 93.78% used; 114375793 free inodes.

server4 `/data`: 31749877760 available bytes; 99.56% used; 225477678 free inodes.

server4 `/tmp`: 111489609728 available bytes; 93.78% used; 114375793 free inodes.

server4 `/var/tmp`: 111489609728 available bytes; 93.78% used; 114375793 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
