# V2R cluster inventory

2026-09-24T06:44:25.261788+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324488626176 available bytes; 81.90% used; 112491526 free inodes.

server1 `/home`: 324488626176 available bytes; 81.90% used; 112491526 free inodes.

server1 `/tmp`: 324488626176 available bytes; 81.90% used; 112491526 free inodes.

server1 `/var/tmp`: 324488626176 available bytes; 81.90% used; 112491526 free inodes.

server1 `/mnt/raid5`: 517572390912 available bytes; 97.63% used; 337723685 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57872265216 available bytes; 96.77% used; 110431193 free inodes.

server2 `/home`: 57872265216 available bytes; 96.77% used; 110431193 free inodes.

server2 `/tmp`: 57872265216 available bytes; 96.77% used; 110431193 free inodes.

server2 `/var/tmp`: 57872265216 available bytes; 96.77% used; 110431193 free inodes.

server2 `/mnt/raid5`: 519805779968 available bytes; 96.41% used; 445191526 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126781497344 available bytes; 92.93% used; 114174926 free inodes.

server3 `/home`: 126781497344 available bytes; 92.93% used; 114174926 free inodes.

server3 `/data`: 139357552640 available bytes; 98.07% used; 225835445 free inodes.

server3 `/tmp`: 126781497344 available bytes; 92.93% used; 114174926 free inodes.

server3 `/var/tmp`: 126781497344 available bytes; 92.93% used; 114174926 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105804660736 available bytes; 94.10% used; 114349239 free inodes.

server4 `/home`: 105804660736 available bytes; 94.10% used; 114349239 free inodes.

server4 `/data`: 315941392384 available bytes; 95.63% used; 225368677 free inodes.

server4 `/tmp`: 105804660736 available bytes; 94.10% used; 114349239 free inodes.

server4 `/var/tmp`: 105804660736 available bytes; 94.10% used; 114349239 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
