# V2R cluster inventory

2026-09-25T11:13:36.505834+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319061950464 available bytes; 82.20% used; 112478861 free inodes.

server1 `/home`: 319061950464 available bytes; 82.20% used; 112478861 free inodes.

server1 `/tmp`: 319061950464 available bytes; 82.20% used; 112478861 free inodes.

server1 `/var/tmp`: 319061950464 available bytes; 82.20% used; 112478861 free inodes.

server1 `/mnt/raid5`: 364878200832 available bytes; 98.33% used; 337554583 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22906265600 available bytes; 98.72% used; 110409988 free inodes.

server2 `/home`: 22906265600 available bytes; 98.72% used; 110409988 free inodes.

server2 `/tmp`: 22906265600 available bytes; 98.72% used; 110409988 free inodes.

server2 `/var/tmp`: 22906265600 available bytes; 98.72% used; 110409988 free inodes.

server2 `/mnt/raid5`: 328697483264 available bytes; 97.73% used; 445088630 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84140302336 available bytes; 95.30% used; 114155492 free inodes.

server3 `/home`: 84140302336 available bytes; 95.30% used; 114155492 free inodes.

server3 `/data`: 142085328896 available bytes; 98.04% used; 225814463 free inodes.

server3 `/tmp`: 84140302336 available bytes; 95.30% used; 114155492 free inodes.

server3 `/var/tmp`: 84140302336 available bytes; 95.30% used; 114155492 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105612083200 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612083200 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238641426432 available bytes; 96.70% used; 224982119 free inodes.

server4 `/tmp`: 105612083200 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612083200 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
