# V2R cluster inventory

2026-09-27T15:14:34.545392+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304748126208 available bytes; 83.00% used; 112401394 free inodes.

server1 `/home`: 304748126208 available bytes; 83.00% used; 112401394 free inodes.

server1 `/tmp`: 304748126208 available bytes; 83.00% used; 112401394 free inodes.

server1 `/var/tmp`: 304748126208 available bytes; 83.00% used; 112401394 free inodes.

server1 `/mnt/raid5`: 628016922624 available bytes; 97.12% used; 337424021 free inodes.
| server2 | True | ['5', '6', '7'] | [] |

server2 `/`: 13403287552 available bytes; 99.25% used; 110351761 free inodes.

server2 `/home`: 13403287552 available bytes; 99.25% used; 110351761 free inodes.

server2 `/tmp`: 13403287552 available bytes; 99.25% used; 110351761 free inodes.

server2 `/var/tmp`: 13403287552 available bytes; 99.25% used; 110351761 free inodes.

server2 `/mnt/raid5`: 524350861312 available bytes; 96.38% used; 444721097 free inodes.
| server3 | True | ['0', '1', '2'] | [] |

server3 `/`: 78557716480 available bytes; 95.62% used; 114062764 free inodes.

server3 `/home`: 78557716480 available bytes; 95.62% used; 114062764 free inodes.

server3 `/data`: 1326742917120 available bytes; 81.66% used; 225756259 free inodes.

server3 `/tmp`: 78557716480 available bytes; 95.62% used; 114062764 free inodes.

server3 `/var/tmp`: 78557716480 available bytes; 95.62% used; 114062764 free inodes.
| server4 | True | ['1', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 108536778752 available bytes; 93.94% used; 114372725 free inodes.

server4 `/home`: 108536778752 available bytes; 93.94% used; 114372725 free inodes.

server4 `/data`: 350411329536 available bytes; 95.16% used; 224727171 free inodes.

server4 `/tmp`: 108536778752 available bytes; 93.94% used; 114372725 free inodes.

server4 `/var/tmp`: 108536778752 available bytes; 93.94% used; 114372725 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
