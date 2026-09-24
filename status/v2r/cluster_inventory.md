# V2R cluster inventory

2026-09-24T19:10:53.451083+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323993358336 available bytes; 81.93% used; 112481464 free inodes.

server1 `/home`: 323993358336 available bytes; 81.93% used; 112481464 free inodes.

server1 `/tmp`: 323993358336 available bytes; 81.93% used; 112481464 free inodes.

server1 `/var/tmp`: 323993358336 available bytes; 81.93% used; 112481464 free inodes.

server1 `/mnt/raid5`: 416235995136 available bytes; 98.09% used; 337634627 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54464335872 available bytes; 96.96% used; 110411923 free inodes.

server2 `/home`: 54464335872 available bytes; 96.96% used; 110411923 free inodes.

server2 `/tmp`: 54464335872 available bytes; 96.96% used; 110411923 free inodes.

server2 `/var/tmp`: 54464335872 available bytes; 96.96% used; 110411923 free inodes.

server2 `/mnt/raid5`: 495459315712 available bytes; 96.58% used; 445159395 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84406923264 available bytes; 95.29% used; 114156139 free inodes.

server3 `/home`: 84406923264 available bytes; 95.29% used; 114156139 free inodes.

server3 `/data`: 152445108224 available bytes; 97.89% used; 225799826 free inodes.

server3 `/tmp`: 84406923264 available bytes; 95.29% used; 114156139 free inodes.

server3 `/var/tmp`: 84406923264 available bytes; 95.29% used; 114156139 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105660518400 available bytes; 94.10% used; 114348467 free inodes.

server4 `/home`: 105660518400 available bytes; 94.10% used; 114348467 free inodes.

server4 `/data`: 89915985920 available bytes; 98.76% used; 225267260 free inodes.

server4 `/tmp`: 105660518400 available bytes; 94.10% used; 114348467 free inodes.

server4 `/var/tmp`: 105660518400 available bytes; 94.10% used; 114348467 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
