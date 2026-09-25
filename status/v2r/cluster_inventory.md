# V2R cluster inventory

2026-09-25T07:49:02.342717+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318861959168 available bytes; 82.21% used; 112480371 free inodes.

server1 `/home`: 318861959168 available bytes; 82.21% used; 112480371 free inodes.

server1 `/tmp`: 318861959168 available bytes; 82.21% used; 112480371 free inodes.

server1 `/var/tmp`: 318861959168 available bytes; 82.21% used; 112480371 free inodes.

server1 `/mnt/raid5`: 399577796608 available bytes; 98.17% used; 337558217 free inodes.
| server2 | True | ['0'] | [] |

server2 `/`: 22849355776 available bytes; 98.73% used; 110410481 free inodes.

server2 `/home`: 22849355776 available bytes; 98.73% used; 110410481 free inodes.

server2 `/tmp`: 22849355776 available bytes; 98.73% used; 110410481 free inodes.

server2 `/var/tmp`: 22849355776 available bytes; 98.73% used; 110410481 free inodes.

server2 `/mnt/raid5`: 334559981568 available bytes; 97.69% used; 445095884 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84438728704 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84438728704 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142391861248 available bytes; 98.03% used; 225812403 free inodes.

server3 `/tmp`: 84438728704 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84438728704 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637289984 available bytes; 94.11% used; 114350351 free inodes.

server4 `/home`: 105637289984 available bytes; 94.11% used; 114350351 free inodes.

server4 `/data`: 249050214400 available bytes; 96.56% used; 225011467 free inodes.

server4 `/tmp`: 105637289984 available bytes; 94.11% used; 114350351 free inodes.

server4 `/var/tmp`: 105637289984 available bytes; 94.11% used; 114350351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
