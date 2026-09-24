# V2R cluster inventory

2026-09-24T04:53:14.257966+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324621250560 available bytes; 81.89% used; 112492779 free inodes.

server1 `/home`: 324621250560 available bytes; 81.89% used; 112492779 free inodes.

server1 `/tmp`: 324621250560 available bytes; 81.89% used; 112492779 free inodes.

server1 `/var/tmp`: 324621250560 available bytes; 81.89% used; 112492779 free inodes.

server1 `/mnt/raid5`: 474674270208 available bytes; 97.82% used; 337724574 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40767111168 available bytes; 97.73% used; 110430442 free inodes.

server2 `/home`: 40767111168 available bytes; 97.73% used; 110430442 free inodes.

server2 `/tmp`: 40767111168 available bytes; 97.73% used; 110430442 free inodes.

server2 `/var/tmp`: 40767111168 available bytes; 97.73% used; 110430442 free inodes.

server2 `/mnt/raid5`: 523811688448 available bytes; 96.38% used; 445195168 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292389122048 available bytes; 83.68% used; 114200007 free inodes.

server3 `/home`: 292389122048 available bytes; 83.68% used; 114200007 free inodes.

server3 `/data`: 24354287616 available bytes; 99.66% used; 225840548 free inodes.

server3 `/tmp`: 292389122048 available bytes; 83.68% used; 114200007 free inodes.

server3 `/var/tmp`: 292389122048 available bytes; 83.68% used; 114200007 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105835823104 available bytes; 94.09% used; 114349396 free inodes.

server4 `/home`: 105835823104 available bytes; 94.09% used; 114349396 free inodes.

server4 `/data`: 253351694336 available bytes; 96.50% used; 225366845 free inodes.

server4 `/tmp`: 105835823104 available bytes; 94.09% used; 114349396 free inodes.

server4 `/var/tmp`: 105835823104 available bytes; 94.09% used; 114349396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
