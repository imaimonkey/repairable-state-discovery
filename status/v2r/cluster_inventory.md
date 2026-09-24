# V2R cluster inventory

2026-09-24T20:58:53.434573+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323981103104 available bytes; 81.93% used; 112481437 free inodes.

server1 `/home`: 323981103104 available bytes; 81.93% used; 112481437 free inodes.

server1 `/tmp`: 323981103104 available bytes; 81.93% used; 112481437 free inodes.

server1 `/var/tmp`: 323981103104 available bytes; 81.93% used; 112481437 free inodes.

server1 `/mnt/raid5`: 415561080832 available bytes; 98.09% used; 337631101 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30142951424 available bytes; 98.32% used; 110411380 free inodes.

server2 `/home`: 30142951424 available bytes; 98.32% used; 110411380 free inodes.

server2 `/tmp`: 30142951424 available bytes; 98.32% used; 110411380 free inodes.

server2 `/var/tmp`: 30142951424 available bytes; 98.32% used; 110411380 free inodes.

server2 `/mnt/raid5`: 491385503744 available bytes; 96.60% used; 445155955 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84385058816 available bytes; 95.29% used; 114156101 free inodes.

server3 `/home`: 84385058816 available bytes; 95.29% used; 114156101 free inodes.

server3 `/data`: 150903517184 available bytes; 97.91% used; 225803783 free inodes.

server3 `/tmp`: 84385058816 available bytes; 95.29% used; 114156101 free inodes.

server3 `/var/tmp`: 84385058816 available bytes; 95.29% used; 114156101 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105639133184 available bytes; 94.10% used; 114348376 free inodes.

server4 `/home`: 105639133184 available bytes; 94.10% used; 114348376 free inodes.

server4 `/data`: 77021347840 available bytes; 98.94% used; 225255404 free inodes.

server4 `/tmp`: 105639133184 available bytes; 94.10% used; 114348376 free inodes.

server4 `/var/tmp`: 105639133184 available bytes; 94.10% used; 114348376 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
