# V2R cluster inventory

2026-09-25T04:29:01.505681+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318928924672 available bytes; 82.21% used; 112480378 free inodes.

server1 `/home`: 318928924672 available bytes; 82.21% used; 112480378 free inodes.

server1 `/tmp`: 318928924672 available bytes; 82.21% used; 112480378 free inodes.

server1 `/var/tmp`: 318928924672 available bytes; 82.21% used; 112480378 free inodes.

server1 `/mnt/raid5`: 408738578432 available bytes; 98.12% used; 337591824 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22956265472 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22956265472 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22956265472 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22956265472 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 463097618432 available bytes; 96.80% used; 445110307 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341690368 available bytes; 95.29% used; 114156080 free inodes.

server3 `/home`: 84341690368 available bytes; 95.29% used; 114156080 free inodes.

server3 `/data`: 143532662784 available bytes; 98.02% used; 225816167 free inodes.

server3 `/tmp`: 84341690368 available bytes; 95.29% used; 114156080 free inodes.

server3 `/var/tmp`: 84341690368 available bytes; 95.29% used; 114156080 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105671409664 available bytes; 94.10% used; 114350859 free inodes.

server4 `/home`: 105671409664 available bytes; 94.10% used; 114350859 free inodes.

server4 `/data`: 32803790848 available bytes; 99.55% used; 224963005 free inodes.

server4 `/tmp`: 105671409664 available bytes; 94.10% used; 114350859 free inodes.

server4 `/var/tmp`: 105671409664 available bytes; 94.10% used; 114350859 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
