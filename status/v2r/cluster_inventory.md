# V2R cluster inventory

2026-09-24T09:13:43.539186+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324470509568 available bytes; 81.90% used; 112489995 free inodes.

server1 `/home`: 324470509568 available bytes; 81.90% used; 112489995 free inodes.

server1 `/tmp`: 324470509568 available bytes; 81.90% used; 112489995 free inodes.

server1 `/var/tmp`: 324470509568 available bytes; 81.90% used; 112489995 free inodes.

server1 `/mnt/raid5`: 503262994432 available bytes; 97.69% used; 337715321 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57777201152 available bytes; 96.78% used; 110430929 free inodes.

server2 `/home`: 57777201152 available bytes; 96.78% used; 110430929 free inodes.

server2 `/tmp`: 57777201152 available bytes; 96.78% used; 110430929 free inodes.

server2 `/var/tmp`: 57777201152 available bytes; 96.78% used; 110430929 free inodes.

server2 `/mnt/raid5`: 514561019904 available bytes; 96.44% used; 445178138 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85888110592 available bytes; 95.21% used; 114199165 free inodes.

server3 `/home`: 85888110592 available bytes; 95.21% used; 114199165 free inodes.

server3 `/data`: 166962532352 available bytes; 97.69% used; 225821226 free inodes.

server3 `/tmp`: 85888110592 available bytes; 95.21% used; 114199165 free inodes.

server3 `/var/tmp`: 85888110592 available bytes; 95.21% used; 114199165 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105758412800 available bytes; 94.10% used; 114349058 free inodes.

server4 `/home`: 105758412800 available bytes; 94.10% used; 114349058 free inodes.

server4 `/data`: 302823522304 available bytes; 95.81% used; 225273337 free inodes.

server4 `/tmp`: 105758412800 available bytes; 94.10% used; 114349058 free inodes.

server4 `/var/tmp`: 105758412800 available bytes; 94.10% used; 114349058 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
