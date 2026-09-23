# V2R cluster inventory

2026-09-23T22:12:06.714636+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325705523200 available bytes; 81.83% used; 112501407 free inodes.

server1 `/home`: 325705523200 available bytes; 81.83% used; 112501407 free inodes.

server1 `/tmp`: 325705523200 available bytes; 81.83% used; 112501407 free inodes.

server1 `/var/tmp`: 325705523200 available bytes; 81.83% used; 112501407 free inodes.

server1 `/mnt/raid5`: 1388109643776 available bytes; 93.63% used; 337739867 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41095004160 available bytes; 97.71% used; 110432652 free inodes.

server2 `/home`: 41095004160 available bytes; 97.71% used; 110432652 free inodes.

server2 `/tmp`: 41095004160 available bytes; 97.71% used; 110432652 free inodes.

server2 `/var/tmp`: 41095004160 available bytes; 97.71% used; 110432652 free inodes.

server2 `/mnt/raid5`: 536682516480 available bytes; 96.29% used; 445207340 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292733247488 available bytes; 83.66% used; 114202087 free inodes.

server3 `/home`: 292733247488 available bytes; 83.66% used; 114202087 free inodes.

server3 `/data`: 82445332480 available bytes; 98.86% used; 225847664 free inodes.

server3 `/tmp`: 292733247488 available bytes; 83.66% used; 114202087 free inodes.

server3 `/var/tmp`: 292733247488 available bytes; 83.66% used; 114202087 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106422648832 available bytes; 94.06% used; 114355187 free inodes.

server4 `/home`: 106422648832 available bytes; 94.06% used; 114355187 free inodes.

server4 `/data`: 300157595648 available bytes; 95.85% used; 225441738 free inodes.

server4 `/tmp`: 106422648832 available bytes; 94.06% used; 114355187 free inodes.

server4 `/var/tmp`: 106422648832 available bytes; 94.06% used; 114355187 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
