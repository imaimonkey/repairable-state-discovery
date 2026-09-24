# V2R cluster inventory

2026-09-24T08:20:50.049203+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324403777536 available bytes; 81.90% used; 112490544 free inodes.

server1 `/home`: 324403777536 available bytes; 81.90% used; 112490544 free inodes.

server1 `/tmp`: 324403777536 available bytes; 81.90% used; 112490544 free inodes.

server1 `/var/tmp`: 324403777536 available bytes; 81.90% used; 112490544 free inodes.

server1 `/mnt/raid5`: 510274113536 available bytes; 97.66% used; 337721297 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57811357696 available bytes; 96.77% used; 110431022 free inodes.

server2 `/home`: 57811357696 available bytes; 96.77% used; 110431022 free inodes.

server2 `/tmp`: 57811357696 available bytes; 96.77% used; 110431022 free inodes.

server2 `/var/tmp`: 57811357696 available bytes; 96.77% used; 110431022 free inodes.

server2 `/mnt/raid5`: 516433014784 available bytes; 96.43% used; 445179820 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85899268096 available bytes; 95.21% used; 114200194 free inodes.

server3 `/home`: 85899268096 available bytes; 95.21% used; 114200194 free inodes.

server3 `/data`: 175139926016 available bytes; 97.58% used; 225823155 free inodes.

server3 `/tmp`: 85899268096 available bytes; 95.21% used; 114200194 free inodes.

server3 `/var/tmp`: 85899268096 available bytes; 95.21% used; 114200194 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769795584 available bytes; 94.10% used; 114349144 free inodes.

server4 `/home`: 105769795584 available bytes; 94.10% used; 114349144 free inodes.

server4 `/data`: 280474439680 available bytes; 96.12% used; 225350816 free inodes.

server4 `/tmp`: 105769795584 available bytes; 94.10% used; 114349144 free inodes.

server4 `/var/tmp`: 105769795584 available bytes; 94.10% used; 114349144 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
