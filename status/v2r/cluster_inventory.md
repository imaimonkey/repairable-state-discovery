# V2R cluster inventory

2026-09-24T23:28:36.791480+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319013539840 available bytes; 82.20% used; 112480782 free inodes.

server1 `/home`: 319013539840 available bytes; 82.20% used; 112480782 free inodes.

server1 `/tmp`: 319013539840 available bytes; 82.20% used; 112480782 free inodes.

server1 `/var/tmp`: 319013539840 available bytes; 82.20% used; 112480782 free inodes.

server1 `/mnt/raid5`: 415235026944 available bytes; 98.10% used; 337613394 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23112036352 available bytes; 98.71% used; 110410806 free inodes.

server2 `/home`: 23112036352 available bytes; 98.71% used; 110410806 free inodes.

server2 `/tmp`: 23112036352 available bytes; 98.71% used; 110410806 free inodes.

server2 `/var/tmp`: 23112036352 available bytes; 98.71% used; 110410806 free inodes.

server2 `/mnt/raid5`: 486452948992 available bytes; 96.64% used; 445151262 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84369211392 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84369211392 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148308598784 available bytes; 97.95% used; 225800943 free inodes.

server3 `/tmp`: 84369211392 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84369211392 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799626752 available bytes; 94.10% used; 114348305 free inodes.

server4 `/home`: 105799626752 available bytes; 94.10% used; 114348305 free inodes.

server4 `/data`: 61367373824 available bytes; 99.15% used; 225149624 free inodes.

server4 `/tmp`: 105799626752 available bytes; 94.10% used; 114348305 free inodes.

server4 `/var/tmp`: 105799626752 available bytes; 94.10% used; 114348305 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
