# V2R cluster inventory

2026-09-25T11:47:13.641592+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319058493440 available bytes; 82.20% used; 112478818 free inodes.

server1 `/home`: 319058493440 available bytes; 82.20% used; 112478818 free inodes.

server1 `/tmp`: 319058493440 available bytes; 82.20% used; 112478818 free inodes.

server1 `/var/tmp`: 319058493440 available bytes; 82.20% used; 112478818 free inodes.

server1 `/mnt/raid5`: 364348497920 available bytes; 98.33% used; 337549174 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22906437632 available bytes; 98.72% used; 110409975 free inodes.

server2 `/home`: 22906437632 available bytes; 98.72% used; 110409975 free inodes.

server2 `/tmp`: 22906437632 available bytes; 98.72% used; 110409975 free inodes.

server2 `/var/tmp`: 22906437632 available bytes; 98.72% used; 110409975 free inodes.

server2 `/mnt/raid5`: 326596972544 available bytes; 97.74% used; 445082813 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84212776960 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84212776960 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142042664960 available bytes; 98.04% used; 225813375 free inodes.

server3 `/tmp`: 84212776960 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84212776960 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105602662400 available bytes; 94.11% used; 114350249 free inodes.

server4 `/home`: 105602662400 available bytes; 94.11% used; 114350249 free inodes.

server4 `/data`: 232580993024 available bytes; 96.79% used; 224974848 free inodes.

server4 `/tmp`: 105602662400 available bytes; 94.11% used; 114350249 free inodes.

server4 `/var/tmp`: 105602662400 available bytes; 94.11% used; 114350249 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
