# V2R cluster inventory

2026-09-26T01:03:19.216547+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318659682304 available bytes; 82.22% used; 112476294 free inodes.

server1 `/home`: 318659682304 available bytes; 82.22% used; 112476294 free inodes.

server1 `/tmp`: 318659682304 available bytes; 82.22% used; 112476294 free inodes.

server1 `/var/tmp`: 318659682304 available bytes; 82.22% used; 112476294 free inodes.

server1 `/mnt/raid5`: 345559900160 available bytes; 98.41% used; 337546691 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940086272 available bytes; 98.72% used; 110406200 free inodes.

server2 `/home`: 22940086272 available bytes; 98.72% used; 110406200 free inodes.

server2 `/tmp`: 22940086272 available bytes; 98.72% used; 110406200 free inodes.

server2 `/var/tmp`: 22940086272 available bytes; 98.72% used; 110406200 free inodes.

server2 `/mnt/raid5`: 294121488384 available bytes; 97.97% used; 445056789 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84336623616 available bytes; 95.29% used; 114152424 free inodes.

server3 `/home`: 84336623616 available bytes; 95.29% used; 114152424 free inodes.

server3 `/data`: 124936396800 available bytes; 98.27% used; 225818474 free inodes.

server3 `/tmp`: 84336623616 available bytes; 95.29% used; 114152424 free inodes.

server3 `/var/tmp`: 84336623616 available bytes; 95.29% used; 114152424 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105281671168 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281671168 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141768417280 available bytes; 98.04% used; 224917338 free inodes.

server4 `/tmp`: 105281671168 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281671168 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
