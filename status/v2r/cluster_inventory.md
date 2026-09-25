# V2R cluster inventory

2026-09-25T18:26:20.438852+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318749294592 available bytes; 82.22% used; 112476344 free inodes.

server1 `/home`: 318749294592 available bytes; 82.22% used; 112476344 free inodes.

server1 `/tmp`: 318749294592 available bytes; 82.22% used; 112476344 free inodes.

server1 `/var/tmp`: 318749294592 available bytes; 82.22% used; 112476344 free inodes.

server1 `/mnt/raid5`: 371190923264 available bytes; 98.30% used; 337541893 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23097843712 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23097843712 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23097843712 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23097843712 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 314094428160 available bytes; 97.83% used; 445066735 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84391411712 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84391411712 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 131456385024 available bytes; 98.18% used; 225809909 free inodes.

server3 `/tmp`: 84391411712 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84391411712 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105615970304 available bytes; 94.11% used; 114349601 free inodes.

server4 `/home`: 105615970304 available bytes; 94.11% used; 114349601 free inodes.

server4 `/data`: 229703507968 available bytes; 96.83% used; 224931835 free inodes.

server4 `/tmp`: 105615970304 available bytes; 94.11% used; 114349601 free inodes.

server4 `/var/tmp`: 105615970304 available bytes; 94.11% used; 114349601 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
