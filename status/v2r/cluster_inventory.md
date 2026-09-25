# V2R cluster inventory

2026-09-25T07:38:19.135047+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872440832 available bytes; 82.21% used; 112480372 free inodes.

server1 `/home`: 318872440832 available bytes; 82.21% used; 112480372 free inodes.

server1 `/tmp`: 318872440832 available bytes; 82.21% used; 112480372 free inodes.

server1 `/var/tmp`: 318872440832 available bytes; 82.21% used; 112480372 free inodes.

server1 `/mnt/raid5`: 399618658304 available bytes; 98.17% used; 337558359 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22860267520 available bytes; 98.72% used; 110410516 free inodes.

server2 `/home`: 22860267520 available bytes; 98.72% used; 110410516 free inodes.

server2 `/tmp`: 22860267520 available bytes; 98.72% used; 110410516 free inodes.

server2 `/var/tmp`: 22860267520 available bytes; 98.72% used; 110410516 free inodes.

server2 `/mnt/raid5`: 334918909952 available bytes; 97.69% used; 445096561 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84437123072 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84437123072 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142393995264 available bytes; 98.03% used; 225812579 free inodes.

server3 `/tmp`: 84437123072 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84437123072 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637609472 available bytes; 94.11% used; 114350351 free inodes.

server4 `/home`: 105637609472 available bytes; 94.11% used; 114350351 free inodes.

server4 `/data`: 249068408832 available bytes; 96.56% used; 225013091 free inodes.

server4 `/tmp`: 105637609472 available bytes; 94.11% used; 114350351 free inodes.

server4 `/var/tmp`: 105637609472 available bytes; 94.11% used; 114350351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
