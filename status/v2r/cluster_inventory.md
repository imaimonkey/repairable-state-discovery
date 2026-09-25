# V2R cluster inventory

2026-09-25T02:35:02.147021+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318959865856 available bytes; 82.21% used; 112480413 free inodes.

server1 `/home`: 318959865856 available bytes; 82.21% used; 112480413 free inodes.

server1 `/tmp`: 318959865856 available bytes; 82.21% used; 112480413 free inodes.

server1 `/var/tmp`: 318959865856 available bytes; 82.21% used; 112480413 free inodes.

server1 `/mnt/raid5`: 416202768384 available bytes; 98.09% used; 337605365 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23009128448 available bytes; 98.72% used; 110410437 free inodes.

server2 `/home`: 23009128448 available bytes; 98.72% used; 110410437 free inodes.

server2 `/tmp`: 23009128448 available bytes; 98.72% used; 110410437 free inodes.

server2 `/var/tmp`: 23009128448 available bytes; 98.72% used; 110410437 free inodes.

server2 `/mnt/raid5`: 482958319616 available bytes; 96.66% used; 445113462 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350685184 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84350685184 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145521651712 available bytes; 97.99% used; 225810968 free inodes.

server3 `/tmp`: 84350685184 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84350685184 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105895657472 available bytes; 94.09% used; 114350966 free inodes.

server4 `/home`: 105895657472 available bytes; 94.09% used; 114350966 free inodes.

server4 `/data`: 7897010176 available bytes; 99.89% used; 224968955 free inodes.

server4 `/tmp`: 105895657472 available bytes; 94.09% used; 114350966 free inodes.

server4 `/var/tmp`: 105895657472 available bytes; 94.09% used; 114350966 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
