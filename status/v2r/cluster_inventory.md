# V2R cluster inventory

2026-09-26T01:00:16.175222+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318658400256 available bytes; 82.22% used; 112476292 free inodes.

server1 `/home`: 318658400256 available bytes; 82.22% used; 112476292 free inodes.

server1 `/tmp`: 318658400256 available bytes; 82.22% used; 112476292 free inodes.

server1 `/var/tmp`: 318658400256 available bytes; 82.22% used; 112476292 free inodes.

server1 `/mnt/raid5`: 345564905472 available bytes; 98.41% used; 337546699 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22942105600 available bytes; 98.72% used; 110406204 free inodes.

server2 `/home`: 22942105600 available bytes; 98.72% used; 110406204 free inodes.

server2 `/tmp`: 22942105600 available bytes; 98.72% used; 110406204 free inodes.

server2 `/var/tmp`: 22942105600 available bytes; 98.72% used; 110406204 free inodes.

server2 `/mnt/raid5`: 294202118144 available bytes; 97.97% used; 445056691 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84336881664 available bytes; 95.29% used; 114152424 free inodes.

server3 `/home`: 84336881664 available bytes; 95.29% used; 114152424 free inodes.

server3 `/data`: 124938321920 available bytes; 98.27% used; 225818551 free inodes.

server3 `/tmp`: 84336881664 available bytes; 95.29% used; 114152424 free inodes.

server3 `/var/tmp`: 84336881664 available bytes; 95.29% used; 114152424 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105281736704 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281736704 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141769265152 available bytes; 98.04% used; 224917340 free inodes.

server4 `/tmp`: 105281736704 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281736704 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
