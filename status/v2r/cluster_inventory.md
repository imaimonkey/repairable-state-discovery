# V2R cluster inventory

2026-09-24T10:43:48.570190+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324404391936 available bytes; 81.90% used; 112489173 free inodes.

server1 `/home`: 324404391936 available bytes; 81.90% used; 112489173 free inodes.

server1 `/tmp`: 324404391936 available bytes; 81.90% used; 112489173 free inodes.

server1 `/var/tmp`: 324404391936 available bytes; 81.90% used; 112489173 free inodes.

server1 `/mnt/raid5`: 499787886592 available bytes; 97.71% used; 337696187 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57716428800 available bytes; 96.78% used; 110430469 free inodes.

server2 `/home`: 57716428800 available bytes; 96.78% used; 110430469 free inodes.

server2 `/tmp`: 57716428800 available bytes; 96.78% used; 110430469 free inodes.

server2 `/var/tmp`: 57716428800 available bytes; 96.78% used; 110430469 free inodes.

server2 `/mnt/raid5`: 512366854144 available bytes; 96.46% used; 445174890 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85815033856 available bytes; 95.21% used; 114199440 free inodes.

server3 `/home`: 85815033856 available bytes; 95.21% used; 114199440 free inodes.

server3 `/data`: 164136751104 available bytes; 97.73% used; 225817951 free inodes.

server3 `/tmp`: 85815033856 available bytes; 95.21% used; 114199440 free inodes.

server3 `/var/tmp`: 85815033856 available bytes; 95.21% used; 114199440 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105735622656 available bytes; 94.10% used; 114348964 free inodes.

server4 `/home`: 105735622656 available bytes; 94.10% used; 114348964 free inodes.

server4 `/data`: 132816363520 available bytes; 98.16% used; 225258351 free inodes.

server4 `/tmp`: 105735622656 available bytes; 94.10% used; 114348964 free inodes.

server4 `/var/tmp`: 105735622656 available bytes; 94.10% used; 114348964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
