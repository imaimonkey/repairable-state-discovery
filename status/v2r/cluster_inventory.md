# V2R cluster inventory

2026-09-26T03:00:03.032628+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318417563648 available bytes; 82.24% used; 112476267 free inodes.

server1 `/home`: 318417563648 available bytes; 82.24% used; 112476267 free inodes.

server1 `/tmp`: 318417563648 available bytes; 82.24% used; 112476267 free inodes.

server1 `/var/tmp`: 318417563648 available bytes; 82.24% used; 112476267 free inodes.

server1 `/mnt/raid5`: 331088719872 available bytes; 98.48% used; 337545973 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22942552064 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22942552064 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22942552064 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22942552064 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 288121356288 available bytes; 98.01% used; 445053352 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84309254144 available bytes; 95.30% used; 114152372 free inodes.

server3 `/home`: 84309254144 available bytes; 95.30% used; 114152372 free inodes.

server3 `/data`: 125442621440 available bytes; 98.27% used; 225831196 free inodes.

server3 `/tmp`: 84309254144 available bytes; 95.30% used; 114152372 free inodes.

server3 `/var/tmp`: 84309254144 available bytes; 95.30% used; 114152372 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918849024 available bytes; 94.09% used; 114347151 free inodes.

server4 `/home`: 105918849024 available bytes; 94.09% used; 114347151 free inodes.

server4 `/data`: 109756051456 available bytes; 98.48% used; 224915374 free inodes.

server4 `/tmp`: 105918849024 available bytes; 94.09% used; 114347151 free inodes.

server4 `/var/tmp`: 105918849024 available bytes; 94.09% used; 114347151 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
