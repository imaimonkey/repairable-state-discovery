# V2R cluster inventory

2026-09-26T08:16:28.748427+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318747037696 available bytes; 82.22% used; 112475789 free inodes.

server1 `/home`: 318747037696 available bytes; 82.22% used; 112475789 free inodes.

server1 `/tmp`: 318747037696 available bytes; 82.22% used; 112475789 free inodes.

server1 `/var/tmp`: 318747037696 available bytes; 82.22% used; 112475789 free inodes.

server1 `/mnt/raid5`: 219140173824 available bytes; 98.99% used; 337539023 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22312460288 available bytes; 98.76% used; 110403905 free inodes.

server2 `/home`: 22312460288 available bytes; 98.76% used; 110403905 free inodes.

server2 `/tmp`: 22312460288 available bytes; 98.76% used; 110403905 free inodes.

server2 `/var/tmp`: 22312460288 available bytes; 98.76% used; 110403905 free inodes.

server2 `/mnt/raid5`: 256115326976 available bytes; 98.23% used; 445025309 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82678435840 available bytes; 95.39% used; 114110813 free inodes.

server3 `/home`: 82678435840 available bytes; 95.39% used; 114110813 free inodes.

server3 `/data`: 123918200832 available bytes; 98.29% used; 225829178 free inodes.

server3 `/tmp`: 82678435840 available bytes; 95.39% used; 114110813 free inodes.

server3 `/var/tmp`: 82678435840 available bytes; 95.39% used; 114110813 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106064556032 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106064556032 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89386946560 available bytes; 98.76% used; 224883438 free inodes.

server4 `/tmp`: 106064556032 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106064556032 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
