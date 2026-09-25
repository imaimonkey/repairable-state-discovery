# V2R cluster inventory

2026-09-25T11:22:46.369386+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319063134208 available bytes; 82.20% used; 112478861 free inodes.

server1 `/home`: 319063134208 available bytes; 82.20% used; 112478861 free inodes.

server1 `/tmp`: 319063134208 available bytes; 82.20% used; 112478861 free inodes.

server1 `/var/tmp`: 319063134208 available bytes; 82.20% used; 112478861 free inodes.

server1 `/mnt/raid5`: 364166246400 available bytes; 98.33% used; 337550303 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22913466368 available bytes; 98.72% used; 110409986 free inodes.

server2 `/home`: 22913466368 available bytes; 98.72% used; 110409986 free inodes.

server2 `/tmp`: 22913466368 available bytes; 98.72% used; 110409986 free inodes.

server2 `/var/tmp`: 22913466368 available bytes; 98.72% used; 110409986 free inodes.

server2 `/mnt/raid5`: 327768285184 available bytes; 97.74% used; 445083845 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84140609536 available bytes; 95.30% used; 114155498 free inodes.

server3 `/home`: 84140609536 available bytes; 95.30% used; 114155498 free inodes.

server3 `/data`: 142083317760 available bytes; 98.04% used; 225814322 free inodes.

server3 `/tmp`: 84140609536 available bytes; 95.30% used; 114155498 free inodes.

server3 `/var/tmp`: 84140609536 available bytes; 95.30% used; 114155498 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105611804672 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105611804672 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238628945920 available bytes; 96.70% used; 224980930 free inodes.

server4 `/tmp`: 105611804672 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105611804672 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
