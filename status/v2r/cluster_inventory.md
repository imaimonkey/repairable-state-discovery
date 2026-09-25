# V2R cluster inventory

2026-09-25T05:05:57.781728+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318900285440 available bytes; 82.21% used; 112480331 free inodes.

server1 `/home`: 318900285440 available bytes; 82.21% used; 112480331 free inodes.

server1 `/tmp`: 318900285440 available bytes; 82.21% used; 112480331 free inodes.

server1 `/var/tmp`: 318900285440 available bytes; 82.21% used; 112480331 free inodes.

server1 `/mnt/raid5`: 408615702528 available bytes; 98.13% used; 337571336 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22930944000 available bytes; 98.72% used; 110410436 free inodes.

server2 `/home`: 22930944000 available bytes; 98.72% used; 110410436 free inodes.

server2 `/tmp`: 22930944000 available bytes; 98.72% used; 110410436 free inodes.

server2 `/var/tmp`: 22930944000 available bytes; 98.72% used; 110410436 free inodes.

server2 `/mnt/raid5`: 461932285952 available bytes; 96.81% used; 445109234 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340072448 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84340072448 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 142858575872 available bytes; 98.03% used; 225815433 free inodes.

server3 `/tmp`: 84340072448 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84340072448 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105659191296 available bytes; 94.10% used; 114350406 free inodes.

server4 `/home`: 105659191296 available bytes; 94.10% used; 114350406 free inodes.

server4 `/data`: 27938865152 available bytes; 99.61% used; 224960909 free inodes.

server4 `/tmp`: 105659191296 available bytes; 94.10% used; 114350406 free inodes.

server4 `/var/tmp`: 105659191296 available bytes; 94.10% used; 114350406 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
