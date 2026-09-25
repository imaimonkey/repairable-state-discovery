# V2R cluster inventory

2026-09-25T06:38:21.578431+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872543232 available bytes; 82.21% used; 112480357 free inodes.

server1 `/home`: 318872543232 available bytes; 82.21% used; 112480357 free inodes.

server1 `/tmp`: 318872543232 available bytes; 82.21% used; 112480357 free inodes.

server1 `/var/tmp`: 318872543232 available bytes; 82.21% used; 112480357 free inodes.

server1 `/mnt/raid5`: 399800569856 available bytes; 98.17% used; 337561402 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22886985728 available bytes; 98.72% used; 110410542 free inodes.

server2 `/home`: 22886985728 available bytes; 98.72% used; 110410542 free inodes.

server2 `/tmp`: 22886985728 available bytes; 98.72% used; 110410542 free inodes.

server2 `/var/tmp`: 22886985728 available bytes; 98.72% used; 110410542 free inodes.

server2 `/mnt/raid5`: 370075488256 available bytes; 97.44% used; 445099368 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84450533376 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84450533376 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142537773056 available bytes; 98.03% used; 225813656 free inodes.

server3 `/tmp`: 84450533376 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84450533376 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105639534592 available bytes; 94.10% used; 114350385 free inodes.

server4 `/home`: 105639534592 available bytes; 94.10% used; 114350385 free inodes.

server4 `/data`: 251135909888 available bytes; 96.53% used; 225019290 free inodes.

server4 `/tmp`: 105639534592 available bytes; 94.10% used; 114350385 free inodes.

server4 `/var/tmp`: 105639534592 available bytes; 94.10% used; 114350385 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
