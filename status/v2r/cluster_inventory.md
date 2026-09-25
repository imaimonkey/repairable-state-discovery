# V2R cluster inventory

2026-09-25T06:49:18.113073+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871572480 available bytes; 82.21% used; 112480370 free inodes.

server1 `/home`: 318871572480 available bytes; 82.21% used; 112480370 free inodes.

server1 `/tmp`: 318871572480 available bytes; 82.21% used; 112480370 free inodes.

server1 `/var/tmp`: 318871572480 available bytes; 82.21% used; 112480370 free inodes.

server1 `/mnt/raid5`: 399734525952 available bytes; 98.17% used; 337560553 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22877388800 available bytes; 98.72% used; 110410526 free inodes.

server2 `/home`: 22877388800 available bytes; 98.72% used; 110410526 free inodes.

server2 `/tmp`: 22877388800 available bytes; 98.72% used; 110410526 free inodes.

server2 `/var/tmp`: 22877388800 available bytes; 98.72% used; 110410526 free inodes.

server2 `/mnt/raid5`: 338188845056 available bytes; 97.66% used; 445098731 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84448854016 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84448854016 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142525149184 available bytes; 98.03% used; 225813412 free inodes.

server3 `/tmp`: 84448854016 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84448854016 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105639129088 available bytes; 94.10% used; 114350364 free inodes.

server4 `/home`: 105639129088 available bytes; 94.10% used; 114350364 free inodes.

server4 `/data`: 249509728256 available bytes; 96.55% used; 225018011 free inodes.

server4 `/tmp`: 105639129088 available bytes; 94.10% used; 114350364 free inodes.

server4 `/var/tmp`: 105639129088 available bytes; 94.10% used; 114350364 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
